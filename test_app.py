import argparse


def test_app(py_file):
    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    # Load file here
    with open('input.txt', 'r') as f:
        input_values = f.readlines()

    input_values = list(
        map(lambda x: x.replace('\n', '').strip(), input_values))

    # Load output here
    with open('output.txt', 'r') as f:
        output_values = f.readlines()

    output_values = list(
        map(lambda x: x.replace('\n', '').strip(), output_values))

    output = []

    app = __import__(py_file)
    app.input = mock_input
    app.print = lambda s: output.append(s)
    app.main()

    output = [val for val in output if val != '']

    for (out, res) in zip(output, output_values):
        assert out == res, "your answer: {} - answer key: {}".format(out, res)
    print("Pass all")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--file", required=True,
                        help='python script to run test')
    args = parser.parse_args()

    py_file = args.file
    py_file = py_file.split('/')[-1].split('.')[0]
    test_app(py_file)
