# Shift N bases  
Đây là challenge mình chuẩn bị cho CTF Training của CLB ISP.
  
### Challenge
Cháu ngoan Bác Hồ thì phải luôn ghi nhớ 19051890!  
[ciphertext](/files/shiftNbases.txt)
  
### Writeup  
  
Bài này mình sử dụng `python3.7` để viết script decode.  
  
Trong file được cho chứa một chuỗi số khá dài, nhìn qua thì có cả mã hex. Phán đoán bước đầu, đây sẽ là text sau khi đã encode bằng các base cơ bản.  
Trong các base cơ bản, có các khoảng giá trị đặc biệt cần chú ý như sau:  
| ASCII | OCT | DEC | HEX |
|------|------|------|------|
| All | `1o` - `377o` | `1d` - `255d` | `1h` - `ffh` |
| `A` - `z` | `101o` - `172o` | `65d` - `122d` | `41h` - `7ah` |
| `0` - `9` | `60o` - `71o` | `48d` - `57d` | `30h` - `39h` |  
  
Sau khi xem xét kỹ lưỡng, ta nhận ra đoạn text có vẻ được mã hóa theo quy luật `oct - dec - hex - dec`. Bởi, các số thứ 0, 4, 8,... thường có giá trị lớn nhất, trùng với khoảng giá trị các chữ cái trong hệ `oct`, số thứ 1, 3, 5, 7, 9,.. thường trùng với khoảng giá trị các chữ cái trong hệ `dec`, và các số thứ 2, 6, 10,... thường khá nhỏ so với các giá trị khác, và trùng với khoảng giá trị các chữ cái trong hệ `hex`.  
  
Decode thử xem ra gì?  
  
```python
f = open("shiftNbases.txt", "r")
cipher = f.read().split()
f.close()

base = [8, 10, 16, 10]
text = ""
for i in range(0, len(cipher)):
    text += chr(int(cipher[i], base[i % 4]))
    
print(text)
```  
  
Và ta được output trông như thế này:  
  
```
ISP_IN_YOUR_AREAh|phk}Y{SjtdbiVmnr_sf}fi^mez^{ISP_IN_YOUR_AREA`nghrf^kf_p~yjmgYimq_i`v^.^]atISP_IN_YOUR_AREA^pfa^lht^pf_mqusfghuxnndjpfnfhISP_IN_YOUR_AREAan^kf_sqedwid_oqar^llobD_yqwegISP_IN_YOUR_AREA^whzmoVqtes^ip,^lodp}pemhdznkISP_IN_YOUR_AREAVsnwg1^ylydw_ytg[o^adp}pemhmzISP_IN_YOUR_AREAtgZathhfmpVpg~c3^Tfi^kay^pl_`ISP_IN_YOUR_AREA_t^|iomp_g`vVTtes^v^omhDtbgcaISP_IN_YOUR_AREAohnflg(76?_htiVntxcdL%_R~ydqwISP_IN_YOUR_AREAeg^{a1^kXu^jydbwVy^wgmhiVl`C_yISP_IN_YOUR_AREA`|Vc`hcfbg[amhttbgkrdw_ygmVghxISP_IN_YOUR_AREAidcml_rrnm^zX_arnm^lXnf5_i`vVtISP_IN_YOUR_AREAnl_s`wVctwgdbwVqtes^{fnf5_vtISP_IN_YOUR_AREA\n^|usfgjunwgduiVqtes^|l_cx.dISP_IN_YOUR_AREAAie_S~yjmgegnw_Sgie_p~yjmgma^MISP_IN_YOUR_AREAas^ylydw_htiVC`lhdlieg^YhfogeaISP_IN_YOUR_AREAlh1<89Vctwgdmw`:^WgznqVt`hsnmpISP_IN_YOUR_AREAVr`htz^lf_uj_ghv__cjnl^~\_p~yjISP_IN_YOUR_AREAmgcohD_{`ggh`r_qtwe_k~os^llobhISP_IN_YOUR_AREAtz^lf_uj_ghv__cjnl^~\_p~yjmgcoISP_IN_YOUR_AREAh7_Ingca^whzmoVldhpm`qVkgxnl^iISP_IN_YOUR_AREA`_bqon^kXi^mutb6t
```  
  
Một chuỗi text dài các ký tự kỳ quặc và chèn thêm rất nhiều chuỗi `ISP_IN_YOUR_AREA`. Hẳn là chuỗi này chỉ có tác dụng obfuscate đoạn cipher thôi. Bỏ nó đi:  
  
```python
text = text.replace('ISP_IN_YOUR_AREA', '')
```  
  
Vấn đề còn lại là decrypt đoạn text còn lại sau khi đã deobfuscate. Tên đề bài là `shift and bases`, bước đầu đã là trộn các base, vậy bước này là một dạng của `shifting cipher`?  
  
Flag có form `ispclub{this_is_flag}`. Vậy chắc chắn những ký tự đầu `h|phk}Y{` sau khi decode sẽ phải là `ispclub{`.  Phân tích quy luật của nó:  
  
| Plaintext | Ciphertext |
| ------ | ------ |
| `i` - `105d` | `h` - `104d` |
| `s` - `115d` | `\|` - `124d` |
| `p` - `112d` | `p` - `112d` |
| `c` - `99d` | `h` - `104d` |
| `l` - `108d` | `k` - `107d` |
| `u` - `117d` | `}` - `125d` |
| `b` - `98d` | `Y` - `89d` |
| `{` - `123d` | `{` - `123d` |  
  
Vậy là có liên quan tới con số `19051890` thật. Cụ thể:  
`i` - `1` = `h`  
`s` + `9` = `|`  
...  
  Vậy là các ký tự sẽ được shift theo quy luật dãy số `19051890`, xen kẽ `-` và `+`.  
Tiếp tục decode:  
  
```python
shiftkey = '19051890'
for i in range(0, len(text)):
    if i % 2 == 0:
        plain += chr(ord(text[i]) + int(shiftkey[i % 8]))
    else:
        plain += chr(ord(text[i]) - int(shiftkey[i % 8]))
```  
  
[source](writeupfiles/shiftNbases.py)
  
Flag:   
```
ispclub{Tat_ca_moi_nguoi_deu_sinh_ra_co_quyen_binh_dang._Tao_hoa_cho_ho_nhung_quyen_khong_ai_co_the_xam_pham_duoc;_trong_nhung_quyen_ay,_co_quyen_duoc_song,_quyen_tu_do_va_quyen_muu_cau_hanh_phuc._Loi_bat_hu_ay_o_trong_ban_Tuyen_ngon_Doc_lap_nam_1776_cua_nuoc_My._Suy_rong_ra,_cau_ay_co_y_nghia_la:_tat_ca_cac_dan_toc_tren_the_gioi_deu_sinh_ra_binh_dang,_dan_toc_nao_cung_co_quyen_song,_quyen_sung_suong_va_quyen_tu_do._Ban_Tuyen_ngon_Nhan_quyen_va_Dan_quyen_cua_Cach_mang_Phap_nam_1791_cung_noi:_Nguoi_ta_sinh_ra_tu_do_va_binh_dang_ve_quyen_loi;_va_phai_luon_luon_duoc_tu_do_va_binh_dang_ve_quyen_loi._Do_la_nhung_le_phai_khong_ai_choi_cai_duoc.}
```  
