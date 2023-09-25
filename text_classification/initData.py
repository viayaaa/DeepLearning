import pandas as pd
import numpy as np

bbc_text_df = pd.read_csv('./bbc-text.csv')

# bbc_text_df.head()


df = pd.DataFrame(bbc_text_df)

np.random.seed(112)

df_train, df_val, df_test = np.split(df.sample(frac=1, random_state=42),

                                     [int(.8 * len(df)), int(.9 * len(df))])

print(len(df_train), len(df_val), len(df_test))
