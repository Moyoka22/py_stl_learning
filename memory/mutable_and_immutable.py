


import logging
import sys
FORMAT = '%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s'
HANDLERS = (logging.StreamHandler(sys.stdout),)
logging.basicConfig(format=FORMAT,handlers=HANDLERS,level=logging.INFO)

def afunc(list_param : list, tuple_param : tuple):
    logging.info(f'The id of l is: {id(list_param)}')
    logging.info(f'The id of t is: {id(tuple_param)}')
    list_param = [1,2,3,4] # * This changes the object bound to the name list_param changing the id since this is a new object
    tuple_param = (1,2,3,4) # * This changes the object bound to the name tuple_param changing the id since this is a new object
    logging.info(f'The id of l is: {id(list_param)}')
    logging.info(f'The id of t is: {id(tuple_param)}')

def afunc2(list_param : list, tuple_param : tuple):
    logging.info(f'The id of l is: {id(list_param)}')
    logging.info(f'The id of t is: {id(tuple_param)}')
    list_param.append(6) # * The name points to the same object as in the calling scope thus calling append changes the list
    # ! Tuples are immutable, they do not have any methods which can alter their contents
    # ! and so the object bound to in the calling scope cannot be changed in function scope
    logging.info(f'The id of l is: {id(list_param)}')
    logging.info(f'The id of t is: {id(tuple_param)}')


def main():
    
    l = [1,2,3,4,5]
    t = (1,2,3,4,5)
    logging.info(f'The id of l is: {id(l)}')
    logging.info(f'The id of t is: {id(t)}')
    afunc(l,t)
    logging.info(f'l is {l}')
    logging.info(f't is {t}')
    logging.info(f'The id of l is: {id(l)}')
    logging.info(f'The id of t is: {id(t)}')
    afunc2(l,t)
    logging.info(f'l is {l}')
    logging.info(f't is {t}')
    logging.info(f'The id of l is: {id(l)}')
    logging.info(f'The id of t is: {id(t)}')

if __name__ == '__main__':
    main()