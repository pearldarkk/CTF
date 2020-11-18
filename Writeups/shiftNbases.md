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
