"""This script splits the dataset according to Cross-Validation technique.

It creates new files and saves them in a folder, but it is important to create the folder before running the code and to input the files that are supposed to be splitted.
This tool accepts only .txt files as input and needs the sklearn library.
This file can also be imported as a module and contains only one function:

    * create_cross_validation_files - create files to train and test the model for the Cross-Validation technique
"""

from sklearn.model_selection import PredefinedSplit

def create_cross_validation_files(X, dataset_data, dataset_label, test_fold):
    """Create files to train and test the model for the Cross-Validation technique

    Keyword arguments: 
    X -- files for train and base for PredefinedSplit function
    dataset_data -- files with data for test 
    dataset_label -- files with label for test
    test_fold -- array to predefine the split for Cross-Validation
    """
    ps = PredefinedSplit(test_fold)
    for train_index, test_index in ps.split():
        #print("TRAIN:", train_index, "TEST:", test_index)
        filenames = []
        for i in range(0, (ps.get_n_splits() - 1) ):
            filenames.append(X[train_index[i]])
        print()
        with open('datasets_iob/Cross_Validation/train_CV_' + str(test_index[0]) + '.txt', 'w') as outfile:
            for fname in filenames:
                with open('datasets_iob/' + fname) as infile:
                    for line in infile:
                        outfile.write(line)
        with open('datasets_iob/Cross_Validation/test_data_CV_' + str(test_index[0]) + '.txt', 'w') as outfile:
            with open('datasets_iob/' + dataset_data[test_index[0]]) as infile: 
                for line in infile: 
                    outfile.write(line)
        with open('datasets_iob/Cross_Validation/test_label_CV_' + str(test_index[0]) + '.txt', 'w') as outfile:
            with open('datasets_iob/' + dataset_label[test_index[0]]) as infile: 
                for line in infile: 
                    outfile.write(line)

def main():
    X = ['train_iob_Evernote.txt', 'train_iob_Facebook.txt', 'train_iob_Netflix.txt', 'train_iob_PhotoEditor.txt', 
         'train_iob_Spotify.txt', 'train_iob_Twitter.txt', 'train_iob_WhatsApp.txt', 'train_iob_eBay.txt']
    dataset_data = ['test_data_Evernote.txt', 'test_data_Facebook.txt', 'test_data_Netflix.txt', 'test_data_PhotoEditor.txt', 
                    'test_data_Spotify.txt', 'test_data_Twitter.txt', 'test_data_WhatsApp.txt', 'test_data_eBay.txt']
    dataset_label = ['test_label_Evernote.txt', 'test_label_Facebook.txt', 'test_label_Netflix.txt', 'test_label_PhotoEditor.txt', 
                    'test_label_Spotify.txt', 'test_label_Twitter.txt', 'test_label_WhatsApp.txt', 'test_label_eBay.txt']
    test_fold = [0, 1, 2, 3, 4, 5, 6, 7]
    create_cross_validation_files(X, dataset_data, dataset_label, test_fold)

if __name__ == '__main__':
    main()