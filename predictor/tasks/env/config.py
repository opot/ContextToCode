"""
config.py

Configuration Variables for the Addition NPI Task => Stores Scratch-Pad Dimensions, Vector/Program
Embedding Information, etc.

!cd "/content/drive/My Drive/app/" && python3 main.py --do_train true --num_epochs 11
"""
import numpy as np
import tensorflow as tf

DATA_PATH_TRAIN = "tasks/env/data/train.pik"
DATA_PATH_TEST = "tasks/env/data/test.pik"
DATA_PATH_ENCODE_MASK = "tasks/env/data/mask"
LOG_PATH = "log/"
CKPT_PATH = "log/1class/Context_getRecources/multyonehot/model-0008.ckpt"
CKPT_PATH_CLASS1 = "log/1class/Cursor_getColumnIndex/models/model-0010.ckpt"
MASK_PATH_CLASS1 = "log/1class/Cursor_getColumnIndex/mask"
CKPT_PATH_CLASS3 = "log/1class/Cursor_close/models/model-0010.ckpt"
MASK_PATH_CLASS3 = "log/1class/Cursor_close/mask"
CKPT_PATH_CLASS2 = "log/1class/Cursor_getString/models/model-0010.ckpt"
MASK_PATH_CLASS2 = "log/1class/Cursor_getString/mask"
CKPT_PATH_CLASS4 = "log/1class/Cursor_getLong/models/model-0010.ckpt"
MASK_PATH_CLASS4 = "log/1class/Cursor_getLong/mask"
CKPT_PATH_CLASS5 = "log/1class/Cursor_getInt/models/model-0010.ckpt"
MASK_PATH_CLASS5 = "log/1class/Cursor_getInt/mask"
DSL_DATA_PATH = "/root/ContextToCode/data/datasets/context.json"
DSL_DOMAIN_PATH = "/root/ContextToCode/data/datasets/domain.json"
TEST_CHUNK_PATH = "dsl/data/test.json"
EVAL_LIMIT = 500

CONFIG = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 10000,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

CONFIG1 = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 4409,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

CONFIG2 = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 8629,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

CONFIG3 = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 4285,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

CONFIG4 = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 4245,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

CONFIG5 = {
    "ENVIRONMENT_ROW": 9,         # Input 1, Input 2, Carry, Output
    "ENVIRONMENT_COL": 9,         # 10-Digit Maximum for Addition Task
    "ENVIRONMENT_DEPTH": 5321,      # Size of each element vector => One-Hot, Options: 0-9

    "ARGUMENT_NUM": 1,            # Maximum Number of Program Arguments
    "ARGUMENT_DEPTH": 75,         # Size of Argument Vector => One-Hot, Options 0-9, Default (10)
    "DEFAULT_ARG_VALUE": 74,      # Default Argument Value

    "PROGRAM_NUM": 10,             # Maximum Number of Subroutines
    "PROGRAM_KEY_SIZE": 10,        # Size of the Program Keys
    "PROGRAM_EMBEDDING_SIZE": 13  # Size of the Program Embeddings
}

PROGRAM_SET = [
    ("MOVE_PTR", 4, 2),       # Moves Pointer (4 options) either left or right (2 options)
    ("WRITE", 2, 10),         # Given Carry/Out Pointer (2 options) writes digit (10 options)
    ("TRANSFORM",),           # Top-Level Add Program (calls children routines)
    ("TRANS1",),              # Single-Digit (Column) Add Operation
    ("LSHIFT",)               # Shifts all Pointers Left (after Single-Digit Add)
]

PROGRAM_ID = {x[0]: i for i, x in enumerate(PROGRAM_SET)}

def get_incoming_shape(incoming):
    """ Returns the incoming data shape """
    if isinstance(incoming, tf.Tensor):
        return incoming.get_shape().as_list()
    elif type(incoming) in [np.array, list, tuple]:
        return np.shape(incoming)
    else:
        raise Exception("Invalid incoming layer.")

class Arguments():             # Program Arguments
    def __init__(self, args, num_args=CONFIG["ARGUMENT_NUM"], arg_depth=CONFIG["ARGUMENT_DEPTH"]):
        self.args = args
        self.arg_vec = np.zeros((num_args, arg_depth), dtype=np.float32)

def get_args(args, arg_in=True):
    if arg_in:
        arg_vec = np.zeros((CONFIG["ARGUMENT_NUM"], CONFIG["ARGUMENT_DEPTH"]), dtype=np.int32)
    else:
        arg_vec = [np.zeros((CONFIG["ARGUMENT_DEPTH"]), dtype=np.int32) for _ in
                   range(CONFIG["ARGUMENT_NUM"])]
    # if len(args) > 0:
    #     for i in range(CONFIG["ARGUMENT_NUM"]):
    #         if i >= len(args):
    #             arg_vec[i][CONFIG["DEFAULT_ARG_VALUE"]] = 1
    #         else:
    #             arg_vec[i][args[i]] = 1
    # else:
    for i in range(CONFIG["ARGUMENT_NUM"]):
        arg_vec[i][CONFIG["DEFAULT_ARG_VALUE"]] = 1
    return arg_vec.flatten() if arg_in else arg_vec

def get_env(data):
    env = np.zeros((CONFIG["ENVIRONMENT_ROW"], CONFIG["ENVIRONMENT_DEPTH"]), dtype=np.int32)

    # print(data)
    for i in range(30):
        if "param_"+str(i) in data:
            env[0][data["param_"+str(i)]] = 1
    
    return env.flatten()


