import argparse

def pars_opt(known=False):
    parser= argparse.ArgumentParser()
    parser.add_argument('--input', type= str, default='hello', help='sampe input parameter')
    return parser.parse_known_args()[0] if known else parser.parse_args()
def sample(opt):
    print(opt.input)

if __name__=='__main__':
    opt= pars_opt()
    sample(opt)
