import os

def GetTitlesAndAuthors():
    # Path to the file
    file_path = 'titleauthor.txt'

    # Creating arrays for titles and composers
    titles = []
    composers = []

    # Reading from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            if ';' in line:  # Making sure the line contains a separator
                title, composer = line.strip().split(';')
                titles.append(title)
                composers.append(composer)
    return (titles,composers)

def GetMusicByIdPath(file_index:int):
    # Path to the music folder
    music_folder = 'music'

    return os.path.join(music_folder, f"{file_index}.mp3")


if(__name__=="__main__"):
    (titles,composers) = GetTitlesAndAuthors()
    # Displaying the arrays
    print("Titles:", titles)
    print("Composers:", composers)

