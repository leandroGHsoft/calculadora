import argparse
import funciones as fn

parser = argparse.ArgumentParser(description='Calculadora, sum/res/mul/div a y b')
parser.add_argument('-a', '--numero_a', type=int, help='Parámetro a')
parser.add_argument('-b', '--numero_b', type=int, help='Parámetro b')
parser.add_argument('-o', '--operacion',
                    type=str,
                    choices=['sum', 'res', 'mul'],
                    default='suma', required=False,
                    help='Operación a realizar con a y b')

args = parser.parse_args()

if args.operacion == 'sum':
    print(args.numero_a + args.numero_b)
elif args.operacion == 'res':
    print(args.numero_a - args.numero_b)
elif args.operacion == 'mul':
    print(args.numero_a * args.numero_b)
elif args.operacion == 'div':
    print(fn.div(args.numero_a, args.numero_b))
