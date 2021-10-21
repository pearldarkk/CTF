# Chuunin Exam

```$ nc 150.230.217.225 2026 ```  
  
Sau intro ngắn thì ta thấy đề bài xuất hiện.  
  
## Stage 1  
  
```
***
First Stage: Written test

Given a ciphertext encrypted using the Roman method of cryptography...



My ciphertext:

Nofovyzon kbyexn 100 LM, xyd exdsv 9dr-moxdebi, Mkockb mszrob gkc mbkmuon gsdr dro nscmyfobi yp pboaeoxmi kxkvicsc.



What is the messages?
````  
  
Tra google với từ khoá tương tự với "Roman encrypt" ta có kết quả là mã hoá Caesar (Caesar Cipher) ở ngay trang đầu.
  
Mã hoá Caesar là kiểu mã hoá bằng phương pháp dịch các chữ cái trong bảng chữ cái đi k ký tự, với k là khoá của mã hoá. 
Ở bài này ta được cho một đoạn mật mã đã mã hoá, nhưng chưa biết key. Ta sẽ tiến hành brute key trong khoảng từ 1 - 25 (Do bảng chữ cái có 26 ký tự) để tìm ra bản rõ.  
  
Ở challenge này, key được sinh ngẫu nhiên. [Decrypt](https://cryptii.com/) với k = 16 ta có plaintext:
```
Developed around 100 BC, not until 9th-century, Caesar cipher was cracked with the discovery of frequency analysis.
```

## Stage 2  
```
***
Second Stage: Forest of Death

You have to bring your team's Scroll to the Building whose position is encrypted by an ancient Greek technique...



My ciphertext:

Lpn_oocScrrcatyyt_pte2tad0el_2dea6_ t_b _ey 



What is the messages?
```
Lần này thì từ khoá ta cần quan tâm sẽ là "Greek encrypt" và cũng dễ dàng xác định đó là kiểu mã hoá Scytale.
Đây là kiểu mã hoá của người Hy Lạp cổ, sử dụng một tấm vải mảnh dài và viết lẻ từng chữ cái lên trên "tấm vải" được tạo ra từ việc cuốn tấm vải quanh một đoạn gỗ. 
Sau khi viết xong, mảnh vải sẽ được gỡ khỏi đoạn gỗ và trở thành đoạn mã tối nghĩa nếu chỉ nhìn tấm vải.  
  
Để giải mã, ta sẽ cần tìm một "đoạn gỗ" có kích thước tương tự với đoạn mà người mã hoá đã sử dụng. [Giải mã](https://dencode.com/cipher/scytale) với "đoạn gỗ" có số ký tự trên một vòng cuốn key = 4 ta có plaintext:
```
Located_at_port_2026_encrypted_by_Scytale  
```

## Stage 3: Final
```
***
Final Stage: Team Fight

The key of teamwork in a fight is to communicate secretly.
This was created at the end of the First World War in German.



Your team using this machine:

_________________________________________________________________

Machine: Enigma M3, reflector UKW B
Rotor - Position - Ring: III - 9 - 3, II - 19 - 20, VI - 16 - 6 
Plugboard: dq cr bi ej kw mt os px uz gh
_________________________________________________________________



My ciphertext:
renoy begxr bczov ukkrg uasgc pkyjw sb



What is the messages? (remove spaces)
```

Tìm kiếm với từ khoá Enigma ta thấy đây là cơ chế mã hoá có nguồn gốc từ Đức, được sử dụng trong thế chiến I và thế chiến II rất nhiều.
Trong bài này thì ta đã được cho chi tiết các thông tin để [decode](https://cryptii.com/) Enigma rất dễ dàng.
Plaintext:
```
enigmaisformilitarycommunication
```

Sau 3 stage ta đã vượt qua challenge và nhận được flag:
```
PTITkagure proud of you as a new Chuunin!
New S-rank Hiden Jutsu to you from ISP Ichizoku: ISPCLUB{s3cr3t_pr0t3ct0r}
```

Flag: ``` ISPCLUB{s3cr3t_pr0t3ct0r} ```