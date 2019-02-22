import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path to input audio stems directory", type=str)
    parser.add_argument("output", help="path to output audio stems directory", type=str)
    args = parser.parse_args()
    main(args)