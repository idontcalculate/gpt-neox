

from megatron.utils import print_rank_0, setup_for_inference_or_eval

from megatron.text_generation_utils import generate_samples_input_from_file, generate_samples_from_prompt, generate_samples_unconditional, generate_samples_interactive

if __name__ == "__main__":
    """
    Generate text/sample model
    """
    model, neox_args = setup_for_inference_or_eval()
    if neox_args.text_gen_type == 'unconditional':
        print_rank_0('Generating samples unconditionally')
        assert neox_args.sample_output_file is not None
        generate_samples_unconditional(
            neox_args=neox_args, 
            model=model,
            number_of_samples=neox_args.num_samples,
            output_file=neox_args.sample_output_file,
            maximum_tokens = neox_args.maximum_tokens, 
            recompute = neox_args.recompute, 
            temperature = neox_args.temperature,
            top_k = neox_args.top_k, 
            top_p = neox_args.top_p
        )

    elif neox_args.text_gen_type == 'input-file':
        print_rank_0(f'Generating samples from input file {neox_args.sample_input_file}')
        assert neox_args.sample_input_file is not None
        generate_samples_input_from_file(
            neox_args=neox_args, 
            model=model,
            input_file=neox_args.sample_input_file,
            output_file=neox_args.sample_output_file,
            maximum_tokens = neox_args.maximum_tokens, 
            recompute = neox_args.recompute, 
            temperature = neox_args.temperature,
            top_k = neox_args.top_k, 
            top_p = neox_args.top_p
        )

    elif neox_args.text_gen_type == 'interactive':
        generate_samples_interactive(
            neox_args=neox_args, 
            model=model,
            recompute = neox_args.recompute, 
            temperature = neox_args.temperature,
            top_k = neox_args.top_k, 
            top_p = neox_args.top_p
        )

    else:
        raise ValueError(f"`text-gen-type` either not specified or not recognised: {neox_args.text_gen_type}")

