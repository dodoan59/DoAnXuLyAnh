Face Detector Using PCA
Nhận dạng khuôn mặt bằng Phân tích thành phần chính - PCA sử dụng 5 ảnh để đào tạo và 1 ảnh để kiểm tra cho 8 người.
Process
Bước1:
Ta sẽ tiến hành hiện chuẩn bị dữ liệu khuôn mặt để xử lý thành dạng vector với 5 bức ảnh của mỗi 8 người.
Sau vòng lặp, face_vector ta thực hiện chuyển vị với hàm transposeđể thu được  một mảng 2D (face_vector) trong đó mỗi cột thể hiện một 
hình ảnh khuôn mặt khác nhau.Mảng này sau đó sẵn sàng cho các bước tiếp theo trong thuật toán nhận dạng khuôn mặt.
Bước 2:
Khi face_vector được hình thành, chúng ta cần tính toán hình ảnh trung bình của tất cả các hình ảnh bằng cách sử dụng phương thức mean 
và trừ nó bởi face_vector. Điều này được thực hiện vì chúng ta cần loại bỏ các đặc điểm chung cho tất cả các hình ảnh.
Bước 3: Tìm ma trận hiệp phương sai. Ma trận hiệp phương sai là một ma trận có phần tử ở vị trí i, j là hiệp phương sai giữa phần tử thứ i và
thứ j của một vectơ ngẫu nhiên.Từ ma trận đó ta sẽ tính được giá trị riêng(eigen_value) và vector riêng (eigen_vector) bằng hàm có sẵn.
Bước 4:
Chọn K vector riêng
Các vectơ riêng đại diện cho các chiều được sắp xếp dựa trên các giá trị riêng của chúng và các chiều K trong số chúng được chọn.Tiếp theo,ta sẽ 
chuyển đổi sang kích thước ban đầu bằng cách chiếu các vectơ mặt đã chuẩn hóa (normalized_face_vector) lên các mặt riêng K để thu được các mặt riêng 
theo chiều ban đầu.Bước này có thể được thực hiện bằng cách nhân các vectơ riêng K được chọn với phép chuyển vị của vectơ mặt chuẩn hóa.
Bước 5: 
Khởi tạo trọng số cho các khuôn mặt riêng trong bộ ảnh huấn luyện bằng cách nhân các mặt riêng với các vectơ mặt chuẩn hóa.Đối với mỗi 
vectơ khuôn mặt huấn luyện, ta có được một tập hợp các trọng số biểu thị mức độ đóng góp của mỗi mặt riêng vào thành phần của khuôn mặt đó.
Từ đó, các trọng số này được sử dụng trong giai đoạn thử nghiệm để tìm ra sự trùng khớp gần nhất giữa trọng số của ảnh thử nghiệm và trọng số của ảnh huấn luyện.
Bước 6: Giai đoạn thử nghiệm:
Tải ảnh thử nghiệm lên tiến hành các bước như ở trên:
Chuyển đổi hình ảnh thử nghiệm đầu vào thành vector khuôn mặt  Chuẩn hóa vector khuôn mặt  chiếu của vectơ lên không gian riêng và tìm trọng số  Tìm chỉ mục (index) 
mà khoảng cách Educide là tối thiểu .Biến chỉ mục trả về mặt huấn luyện được coi là khớp nhất với mặt kiểm tra dựa trên khoảng cách Euclide được tính toán trong không gian trọng số.
Sau khi có được chỉ mục này, các câu lệnh điều kiện tiếp theo trong mã sẽ được sử dụng để gán thông tin về khuôn mặt được xác định dựa trên phạm vi chỉ số được xác định trước. 
Điều này giả định rằng mỗi phạm vi chỉ số tương ứng với một cá nhân cụ thể trong tập dữ liệu.
