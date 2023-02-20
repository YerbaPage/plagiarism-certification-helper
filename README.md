# plagiarism-certification-helper

This is a Python script that allows users to detect **word by word** plagiarism between two input sentences.

## Example

![](https://cdn.mathpix.com/snip/images/PsCoHDZh1aDbDWGvMzTvym8xJn21MQIpvQEF7Vwwdh0.original.fullsize.png)

## Requirements

To run this script, you will need to have Python 3 and the following Python packages installed:

- `streamlit`

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the cloned repository.
3. Run `streamlit run demo.py` to launch the Streamlit app.
4. Input two sentences and click "Enter".
5. The app will highlight the overlapping words.

## How it works

The script uses an n-gram overlap approach, where it breaks each sentence into n-grams (subsequences of n words) and checks for overlap between the two sentences. The default value of n is 3. The script outputs the set of n-grams that appear in both sentences and highlights them in the output.

## Credits

This script was written by Yuling Shi in February 2023. The code is available under the Apache License 2.0.

## References

The following resources were used in the development of this script:

- [Streamlit documentation](https://docs.streamlit.io/)
