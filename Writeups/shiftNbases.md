# Shift N bases  
Đây là challenge mình chuẩn bị cho CTF Training của CLB ISP.
  
### Challenge
Cháu ngoan Bác Hồ thì phải luôn ghi nhớ 19051890!  
[ciphertext](/files/shiftNbases.txt)
  
### Writeup
Trong file được cho chứa một chuỗi số khá dài, nhìn qua thì có cả mã hex. Phán đoán bước đầu, đây sẽ là text sau khi đã encode bằng các base cơ bản.  
Trong các base cơ bản, có các khoảng giá trị đặc biệt cần chú ý như sau:  
| ASCII | OCT | DEC | HEX |
|------|------|------|------|
| All | `1o` - `377o` | `1d` - `255d` | `1h` - `ffh` |
| `A` - `z` | `101o` - `172o` | `65` - `122` | `41` - `7a` |
| `0` - `9` | `60o` - `71o` | `48` - `57` | `30` - `39` |  
  
Sau khi xem xét kỹ lưỡng, ta nhận ra đoạn text có vẻ được mã hóa theo quy luật `oct - dec - hex - dec`. Bởi, các số thứ 0, 4, 8,... thường có giá trị lớn nhất, trùng với khoảng giá trị các chữ cái trong hệ `oct`, số thứ 1, 3, 5, 7, 9,.. thường trùng với khoảng giá trị các chữ cái trong hệ `dec`, và các số thứ 2, 6, 10,... thường khá nhỏ so với các giá trị khác, và trùng với khoảng giá trị các chữ cái trong hệ `hex`.

Sau đó mình viết một đoạn code nhỏ bằng C, sử dụng `scanf` để định dạng input và decode:
```cpp

```
