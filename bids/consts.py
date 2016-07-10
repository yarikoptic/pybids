import os.path as op

__all__ = ['data_path']

data_path = op.join(op.dirname(op.realpath(__file__)), 'data')