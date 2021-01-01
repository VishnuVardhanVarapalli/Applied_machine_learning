import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--training_file",type = str)
    parser.add_argument("--models",type = str)
    
    args = parser.parse_args()
    
    #training file contains input 
    TRAINING_FILE = args.training_file
    
    #Directory for saving output models
    MODELS  = args.models

