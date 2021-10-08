#include <iostream>
#include <string>
using namespace std;

#define EL printf("\n")

string flag = "ispclub{Tat_ca_moi_nguoi_deu_sinh_ra_co_quyen_binh_dang._Tao_hoa_cho_ho_nhung_quyen_khong_ai_co_the_xam_pham_duoc;_trong_nhung_quyen_ay,_co_quyen_duoc_song,_quyen_tu_do_va_quyen_muu_cau_hanh_phuc._Loi_bat_hu_ay_o_trong_ban_Tuyen_ngon_Doc_lap_nam_1776_cua_nuoc_My._Suy_rong_ra,_cau_ay_co_y_nghia_la:_tat_ca_cac_dan_toc_tren_the_gioi_deu_sinh_ra_binh_dang,_dan_toc_nao_cung_co_quyen_song,_quyen_sung_suong_va_quyen_tu_do._Ban_Tuyen_ngon_Nhan_quyen_va_Dan_quyen_cua_Cach_mang_Phap_nam_1791_cung_noi:_Nguoi_ta_sinh_ra_tu_do_va_binh_dang_ve_quyen_loi;_va_phai_luon_luon_duoc_tu_do_va_binh_dang_ve_quyen_loi._Do_la_nhung_le_phai_khong_ai_choi_cai_duoc.}";
string num = "19051890";

void shift(string &s) {
    for (int i = 0; i < s.size(); i += 2) {
        s[i] = (s[i] - (num[i % 8] - 0x30)) % 256;
        s[i + 1] = (s[i + 1] + (num[(i + 1) % 8] - 0x30)) % 256;
    }
}

void obfuscate(string &s) {
    string obfus = "ISP_IN_YOUR_AREA";
    for (int i = 0; i < s.size(); i += 46) 
        s.insert(i, obfus);
}

void bases(string &s) {
    for (int i = 0; i < s.size(); i += 4)
        printf("%o %u %x %u ", (unsigned char) s[i], (unsigned char) s[i + 1], (unsigned char) s[i + 2], (unsigned char) s[i + 3]);
    EL;
}

int main() {
    freopen("shiftNbases.txt", "w", stdout);
    shift(flag);
    obfuscate(flag);
    bases(flag);

    return 0;
}

