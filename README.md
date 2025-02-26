###MOPTIMIZERS
Tested:
Adam
CPUAdam
1-Bit Adam
SM3
Madgrad_wd

Preprocessing:
--input INPUT: Path to input JSON file containing your data.
--json-keys JSON_KEYS [JSON_KEYS ...]: Space-separated list of keys to extract from the JSON. Default: text.
--split-sentences: Split documents into sentences for more granular tokenization.
--keep-newlines: Keep newlines when splitting sentences.
 Tokenizer Settings:
--vocab-file VOCAB_FILE: Path to the vocab file.
--merge-file MERGE_FILE: Path to the BPE merge file (required for some tokenizers).
--append-eod: Append an <eod> token to the end of each document (End of Document marker).

Output Data:
--output-prefix OUTPUT_PREFIX: Path to save the binary output file (without suffix).
--dataset-impl {lazy,cached,mmap}: Choose how to store the dataset: lazy for on-demand loading, cached for faster access, and mmap for memory-mapped storage.

Optional:
Settings:
--workers WORKERS: Number of worker processes to launch for data processing.
--log-interval LOG_INTERVAL: Set the interval between progress updates to keep track of the process.

Results:
worker-based parallelism for speed 

Tips:
Adamx and jax & better tokenizer

idontcalulate
