

char buf[15] = "CTF{";
buf[4] = '0';
buf[5] = -162;
for (int i = 0x1; i < 0xFF; ++i)
if (i + i ^ 212 == 0)
buf[6] = i;
puts(buf);

return 0;
}