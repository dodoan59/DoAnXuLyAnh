import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import customtkinter
from customtkinter import*
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox
# Hàm xử lý khi nhấn button "Ảnh đưa vào"
file_path = ""  # Define file_path as a global variable

# Hàm xử lý khi nhấn button "Ảnh đưa vào"
def open_image():
    global file_path  # Add global keyword to access the global variable
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    if file_path:
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        input_label.configure(image=photo,width=image.width, height=image.height)
        input_label.image = photo

# Hàm xử lý khi nhấn button "Nhận diện khuôn mặt"
def recognize_face():
    status_label.configure(text="TRẠNG THÁI: ĐANG THỰC HIỆN")
    root.update_idletasks()
    global file_path
    image_width = 720
    image_length = 1280
    total_pixels = image_width*image_length
    images = 5
    variants = 8
    total_images = images*variants
    face_vector = []
    for i in range(1, total_images+1):
        face_image = cv2.imread("training/"+ str(i)+ ".jpg")
        face_image = cv2.cvtColor(face_image,cv2.COLOR_RGB2GRAY)
        # plt.imshow(face_image, cmap = 'gray', interpolation = 'bicubic')
        # plt.show()
        face_image = face_image.reshape(total_pixels,)
    
        face_vector.append(face_image)
        
    face_vector = np.asarray(face_vector)
    face_vector = face_vector.transpose()

  

    avg_face_vector = face_vector.mean(axis=1)
    avg_face_vector = avg_face_vector.reshape(face_vector.shape[0], 1)
    normalized_face_vector = face_vector - avg_face_vector


    covariance_matrix = np.cov(np.transpose(normalized_face_vector))
    # covariance_matrix = np.transpose(normalized_face_vector).dot(normalized_face_vector)


    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)



    k = 21
    k_eigen_vectors = eigen_vectors[0:k, :]


    eigen_faces = k_eigen_vectors.dot(np.transpose(normalized_face_vector))


    # weights = eigen_faces.dot(normalized_face_vector)
    weights = np.transpose(normalized_face_vector).dot(np.transpose(eigen_faces))
    if file_path:
        test_img = cv2.imread(file_path)
        test_img_a = cv2.cvtColor(test_img,cv2.COLOR_RGB2GRAY)



        test_img_a = test_img_a.reshape(total_pixels, 1)
        test_normalized_face_vector = test_img_a - avg_face_vector
        test_weight = np.transpose(test_normalized_face_vector).dot(np.transpose(eigen_faces))
        index =  np.argmin(np.linalg.norm(test_weight - weights, axis=1))    
            
        if(index>=0 and index <5):
            info = "HỌ TÊN:ĐOÀN NGỌC ĐÔ \n TUỔI:21 \n NGÀY SINH:05/09/2002 \n NGHỀ NGHIỆP:SINH VIÊN"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
         
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
            
        elif(index>=5 and index<10):
            info = "HỌ TÊN:TRẦN MINH ĐỨC \n TUỔI:22 \n NGÀY SINH:03/10/2000 \n NGHỀ NGHIỆP:TRƯỞNG PHÒNG"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
     
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=10 and index<15):
            info = "HỌ TÊN:LIONEL MESSI \n TUỔI:36 \n NGÀY SINH:24/06/1987 \n NGHỀ NGHIỆP:CẦU THỦ"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
            
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=15 and index<20):
            info = "HỌ TÊN:NHẬT TÂN \n TUỔI:21 \n NGÀY SINH:04/02/2002 \n NGHỀ NGHIỆP:HỌA SĨ"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI

            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=20 and index<25):
            info = "HỌ TÊN:THANH NHÂN \n TUỔI:20 \n NGÀY SINH:03/10/2003 \n NGHỀ NGHIỆP:SÁT THỦ"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
          
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=25 and index<30):
            info = "TÊN:JOHN CENA,TUỔI:30,\n NGHỀ NGHIỆP: ĐẤU VẬT"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
           
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=30 and index<35):
            info = "TÊN:ROSE,TUỔI:30,\n NGHỀ NGHIỆP: IDOL"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
          
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
        elif(index>=35 and index<40):
            info = "TÊN:JENNIE,TUỔI:30,\n NGHỀ NGHIỆP: IDOL"
            info_label.configure(text=info)
            status_label.configure(text="TRẠNG THÁI: THỰC HIỆN THÀNH CÔNG") #TRẠNG THÁI
            
            n = index + 1
            image = Image.open("training/"+ str(n)+ ".jpg")
            image.thumbnail((300, 300))  # Resize hình ảnh cho phù hợp
            photo = ImageTk.PhotoImage(image)
            output_label.configure(image=photo,width=image.width, height=image.height)
            output_label.image = photo
    else:
        CTkMessagebox(title="Lỗi", message="Vui lòng chọn ảnh!!!", icon="cancel")
        status_label.configure(text="TRẠNG THÁI: ")

# Hàm xử lý khi nhấn button "Xóa hết"
def clear_all():
    input_label.configure(image='')
    output_label.configure(image='')
    info_label.configure(text="THÔNG TIN \n CỦA ĐỐI TƯỢNG")
    status_label.configure(text="TRẠNG THÁI: ")
    # Clear global file_path variable
    global file_path
    file_path = ""

    # Reset input_label size
    input_label.configure(width=25, height=18)
    output_label.configure(width=25, height=18)
# Hàm xử lý khi nhấn button "Thoát"
def exit_program():
    root.destroy()

# Tạo cửa sổ chính
root = CTk()
root.configure(background='#0B2758')
root.title("Face Recognition")
root.geometry("1000x580+150+50")
root.configure(fg_color='#0B2758')
customtkinter.set_appearance_mode("dark")
#Top frames
CTkLabel(root,text="Email: do.207ct68625@vanlanguni.vn\nVLU-207CT68625",width=10,height=20,bg_color="#0e63c9",anchor='e',padx=10,pady=10).pack(side='top',fill='both')
CTkLabel(root,text="NHẬN DIỆN KHUÔN MẶT",text_color='yellow',width=10,height=50,bg_color="#fff",fg_color='#175aab',font=('Arial bold',20)).pack(side='top',fill='both')
#MENU FRAMES

menu_frame = CTkFrame(root,border_width=2,border_color='#05255C', width=200, height=0, fg_color='light gray')  
menu_frame.pack(side='left', fill='y')

menu_label = CTkLabel(menu_frame, text="MENU" , font=("Arial bold", 20),width=150,height=40,text_color='white',fg_color='#788DB2',corner_radius=3)  
menu_label.pack(side='top', fill='y',pady=20)


button1 = CTkButton(menu_frame, text="Chọn ảnh đưa vào", command=open_image, width=130, height=50)  
button1.pack(pady=20)  

button2 = CTkButton(menu_frame, text="Nhận diện", command=recognize_face, width=130, height=50)  
button2.pack(pady=20)  

button3 = CTkButton(menu_frame, text="Xóa hết", command=clear_all, width=130, height=50)  
button3.pack(pady=20)   

button4 = CTkButton(menu_frame, text="Thoát", command=exit_program, width=130, height=50)  
button4.pack(pady=20)   

# Tạo phần hiển thị ảnh và kết quả
image_frame = CTkFrame(root, border_width=2,border_color='#05255C', fg_color='light gray', width=200, height=200)
image_frame.pack(side='right', fill='both', expand=True)

# Tạo frame chứa input_text và input_label
label_frame = CTkFrame(image_frame, fg_color='light gray',width=300,height=300)
label_frame.pack(side='left',padx=(150,70) ,pady=(50, 10))
label_frame.place(x=130,y=120)

input_text = tk.Label(label_frame, text="ẢNH NHẬP VÀO", bg="#0e63c9", fg="yellow",width=25,height=2)
input_text.grid(row=0, column=0,pady=10,sticky='e')
custom_font = ("Arial", 9, "bold")
input_text.configure(font=custom_font)
input_text.configure(highlightbackground="white", highlightthickness=2)

input_label = tk.Label(label_frame, text="Input image", bg='white', width=25, height=18, relief="groove")
input_label.grid(row=1, column=0, padx=(50, 0))

output_text = tk.Label(label_frame, text="ẢNH NHẬN DIỆN ĐƯỢC", bg="#0e63c9", fg="yellow",width=25,height=2)
output_text.grid(row=0, column=2,sticky='e')
output_text.configure(font=custom_font)
output_text.configure(highlightbackground="white", highlightthickness=2)

output_label = tk.Label(label_frame, text="Output image", bg='white', width=25, height=18, relief="groove")
output_label.grid(row=1, column=2, padx=(100, 0))

# Tạo đối tượng Label để hiển thị thông tin
info_label = CTkLabel(image_frame, text="THÔNG TIN \n CỦA \n ĐỐI TƯỢNG", font=("Arial bold", 15), width=180, height=250,fg_color='#708090',text_color='orange',corner_radius=5)
info_label.pack(side='right',padx = 30,anchor='e')

#TRẠNG THÁI
status_label = CTkLabel(image_frame, text="TRẠNG THÁI: ", font=("Arial bold", 15),width=350,height=70,fg_color='#175aab',text_color='yellow',corner_radius=10)
status_label.place(x=180, y=10, anchor="nw")

root.mainloop()