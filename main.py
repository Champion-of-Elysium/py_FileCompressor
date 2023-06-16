import PySimpleGUI as gui
from zip_creater import make_archive

lable1 = gui.Text("Select files to compress: ")
input1 = gui.Input()
choose_btn1 = gui.FilesBrowse("Choose", key="files")

lable2 = gui.Text("Select destination folder: ")
input2 = gui.Input()
choose_btn2 = gui.FolderBrowse("Choose", key="folder")

compress_btn = gui.Button("Compress")
output_label = gui.Text(key="output", text_color="yellow")

col1 = gui.Column([[lable1], [lable2]])
col2 = gui.Column([[input1], [input2]])
col3 = gui.Column([[choose_btn1], [choose_btn2]])

window = gui.Window("File Compressor",
                    layout=[[col1, col2, col3], [compress_btn, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            folder = values["folder"]
            make_archive(filepaths, folder)
            window["output"].update(value="Compression Completed!")

        case gui.WIN_CLOSED:
            break
window.close()