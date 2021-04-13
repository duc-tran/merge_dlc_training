Clone or Download this Repo to your Computer

If you have annotated data from DLC, copy the content of labeled-data folders from your DLC projects into the labeled_data folder in this repo.
Run the code.

This code will:
  1.Rename all the images, add the subject name as a prefix to each image
  2.Rename the images' name in the corresponding csv file.
  3.Combine all the csv file into one

If you make some mistake or you want to generate a new Combined_data.csv file, please delete the existing file. Otherwise, an error will pop up. I will fix this later.

After this, you need to create a new DLC project. Choose any videos you want, annotate some of it, even 1 or 2 is okay. Then Copy the Combined_data.csv into the new project's labeled-data, rename the Combined_data.csv to match the existing csv file in that folder, copy all the images from this repo into that folder also.

Last step is run the training process. Now you have the training data that consists of many different baby, in other words, we generalize the training data.

The best practice of testing is to test it on a baby that was not included in the training dataset.

Last but not least, feel free to contact me! Either at trandt@cua.edu or duc.tranthuan@gmail.com
