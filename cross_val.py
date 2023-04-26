import pandas as pd
import csv

def cross_val_writer(array, writer):
    for count in range(10):
        # write a row to the csv file
        fold_num = f'fold{count + 1}'
        writer.writerow([fold_num])
        for row in array[count].values.tolist():
            writer.writerow(row)
        if count < 9:
            writer.writerow([])

def cross_val_array_maker(df):
    array = []
    for i in range(10):
        fold = pd.DataFrame(columns=df.columns)
        for label in ['yes', 'no']:
            df_class = df[df[8] == label]
            fold_size, extra = divmod(len(df_class), 10)
            start = i * fold_size
            end = start + fold_size + (1 if i < extra else 0) 
            fold = pd.concat([fold, df_class[start:end]]).sample(frac=1).reset_index(drop=True)
        array.append(fold)
    return array

def cross_val_main(df):
    with open('pima-folds.csv', 'w', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)

            array = cross_val_array_maker(df)

            cross_val_writer(array, writer)


if __name__ == "__main__":
    df = pd.read_csv('pima.csv', header=None)
    cross_val_main(df)

        


        


