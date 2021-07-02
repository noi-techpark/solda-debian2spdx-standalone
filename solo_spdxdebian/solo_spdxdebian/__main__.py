if __name__ == '__main__':
    import argparse
    from solo_spdxdebian.spdxdebian import Debian2SPDX

    parser = argparse.ArgumentParser()
    parser.add_argument("--orig","-o", help="Path of the required .orig file")
    parser.add_argument("--debian","-d", help="Path of the required .debian file")
    parser.add_argument("--name","-n", help="Name of the output file")
    args = parser.parse_args()

    if(args.orig and args.debian):
        d2s = Debian2SPDX(args.orig, args.debian)
        d2s.generate_SPDX()
        d2s.write_SPDX(args.name)
        print("{} and {} were converted successfully".format(args.orig,args.debian))
    else:
        print("try [-h] for help")

 