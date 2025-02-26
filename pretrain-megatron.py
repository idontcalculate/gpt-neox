
"""MEGATRON"""
from megatron.neox_arguments import NeoXArgs
from megatron.training import pretrain

if __name__ == "__main__":
    neox_args = NeoXArgs.consume_neox_args()
    neox_args.configure_distributed_args()
    neox_args.build_tokenizer()
    neox_args.initialize_tensorboard_writer() 
    pretrain(neox_args=neox_args)
