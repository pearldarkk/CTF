# Furipputon 

Đề bài cho một file source C và một file tên Scroll.  
Đầu tiên là xác định kiểu file Scroll

``` $ file Scroll ```

Output:
```
Scroll: ASCII text
```

Vậy tệp Scroll là một file text ngắn. 

Tiến hành phân tích file source.  
  
```c
#include <stdio.h>                                  
int r=0,x,y=0,    /*                                
nt               \ /                                
c    / \ / ||| /\_                                  
lx  /   X _ _  \ |                                  
u, ^_  / \ \/   /\                                  
dn  \           \_        ]                         
e=   \ .||  /\            =                     p p 
 0 |||   /  ||  ||        f        f       f    r r 
<,  /\          /         tw       t       s s  i i 
sy      <<  ||         i  eh       e       e c  n n 
t=  /\ ___  /   /\     n  li       l       e a  t t 
d0  ||      ||  \/     t  ll       l  {<   k n  f f 
i,             |||        (e s     (  fr   ( f  ( ( 
o   ||  || |     /     tu s( t    usw o; i s (  " " 
.   -/  /   /_ |||   c [[ tg rv   [th rx=f t "  % \ 
h       ||  _/   /  mh111 de{l)   +di (+'( d+%  c n+
>                   aa000 itte; > +il x+ n inc  " "+
 /                  ir000[ns[nytyrrne<=)'<xn,"  , );
 */                 n         =             0     ; 
               main        (       )   {            
                char       v   [                    
                100    ]                   ,  s;    
          int t[100     ]                    ,      
              u[100               ]     ;  u        
                  [                   0             
      ]=ftell(stdin        )       ;                
         while(gets (v    )                 )       
                 {t  [         r ]=                 
             strlen                 (               
               v);y=                                
                 t[         r             ]         
                 >y             ?        t [        
                  r         ]    :   y;             
              u[++r   ]     =                       
        ftell(stdin )   ;                          }
              while          (                    n 
                  <              y        )         
            {for(x=0             ;         x        
            <r;x++) {                           s   
               =' '       ;                         
              if(n<             t        [          
                  x            ]     )    {         
        fseek(stdin    ,u       [     x    ]        
                 +n   ,  0 )                     ;  
        scanf("%c",                          &      
                                       s        )   
                   ;                             }  
       printf("%c",   s                       )     
                                            ;      }
      printf("\n");                 n               
                 ++   ;            }           }
```  
  
Đây là một file C trông khá "lạ" so với code C thông thường. Tiến hành compile thử:  

``` $ gcc flipped.c ```

Thì thấy vẫn compile thành công. Vậy file này đã làm rối trong việc đọc code bằng mắt thường. Ta có thể xử lý bằng cách nhờ đến các code beautifier.  
  
Về nội dung, code này sẽ sử dụng hàm `gets()` để nhận input và tiến hành lật ngược (flip) lại theo đường chéo trên trái - dưới phải.

Tiến hành compile file source và decode thôi!

``` $ gcc flipped.c ```

``` $ ./a.out < Scroll ```
  
Output:
```
      ___                     _                                                          
     -   -_, ,,           ,  - -    /`                                                   
    (  ~/||  ||     _    ||    \\  /    '                     _                          
    (  / ||  ||/\  < \, =||=    \\/    \\  _-_  \\/\\ -_-_   < \, \\/\\                  
     \/==||  ||_<  /-||  ||    ==/\==  || || \\ || || || \\  /-|| || ||                  
     /_ _||  || | (( ||  ||     / \\   || ||/   || || || || (( || || ||                  
    (  - \\, \\,\  \/\\  \\, \\/   \\, \\ \\,/  \\ \\ ||-'   \/\\ \\ \\                  
                                                      |/                                 
                                                      '                                  
 __                                                                                      
|_   _       _   _|  _  _ .   |__|  _  _  .  _ |_   _   _    |_/      _  .  _       _    
|   (_) |_| | ) (_| (- |  .   |  | (_| /_ | (- | ) (_| | )   | \ |_| | ) | | ) \)/ (_|   
                                                                                         
 __          _                            __               __         __                 
/    _   __ (_  _       _   _|  _  _ .   |  \  _ |        /       |  /       |           
\__ (_)     |  (_) |_| | ) (_| (- |  .   |__/ (- |( |_|   \__ |_| |( \__ |_| |(          
                                                                                         
                                           __               __         __                
                                          |  \  _ |        /    _  |  /    _  |          
                                          |__/ (- |( |_|   \__ (_| |( \__ (_| |(         
                                                                                         
 __                        __                 __                                         
/        _  _  _  _  |_   |__)  _   _  _ .   |  \  _ |        |__|  _  |_   _            
\__ |_| |  |  (- | ) |_   |__) (_) _) _) .   |__/ (- |( |_|   |  | (_) | ) (_)           
                                                                                         
 __                                                                                      
/  \ |_ |_   _  _  _ .   |__| .  _        _   _       _    |_/     |_   _   _            
\__/ |_ | ) (- |  _) .   |  | | |  |_| \/ /_ (_| \)/ (_|   | \ |_| | ) (_| | )           
                                                                                         
                                                                                         
                   /\  |   _   _   _      /\  |   _  _  .     |__|  _  .      _ .        
                  /--\ |( (_| | ) (- ,   /--\ |( (- ||| | ,   |  | (_| | |_| |  |        
                                                                       /                 
 __                                           __                                         
|_   _   _   |_ |_   _   |  |  _   _ |  _|   |  \  _   _  .  _   _  |_ .  _   _  |       
|   (_) |    |_ | ) (-   |/\| (_) |  | (_|   |__/ (_) ||| | | ) (_| |_ | (_) | ) .
```

Flag: ``` ISPCLUB{DekuHoho} ```  
  
Một điều đặc biệt là chính file source này cũng đối xứng theo đường chéo trái trên - dưới phải. Thử xem nếu lấy chính source code để làm input ta sẽ có gì?

```$ ./a.out < flipped.c ```

Output: 
```c
#include <stdio.h>                                  
int x,n=0,y=0,    /*                                
nt                 /                                
c    ^  |                                           
lr  /_\ |/ /| |-                                    
u= /   \|\ \| |/                                    
d0                        ]                       p 
e, \ / .   _              =                     p r 
 x  X  |  <_  |/|         f        f       f s  r i 
<, / \ |/ <_  | |         tw       t       s c  i n 
sy  _                  i  eh       e       e a  n t 
t= | \        |        n  li       l       e n  t f 
d0 |_/ /| |/|  /_      t  ll       l  {<   k f  f ( 
i, |   \| | |  _/         (e s     (  fr   ( (  ( " 
o                      tu s( t    usw o; i s "  " \ 
.  /\        | |    m  [[ tg rv   [th rx=f t %  % n 
h  \ /\ |/ /\| |    ac111 de l)   +di (+'( d c  c " 
> \_|\_ |  \/|/|/   ih000 it{e;t> +il x+ n i+"  " )+
 /                  na000[nstny[yrrne<=)'<xnn,  , ;+
 */                  r        =       0        ;    
                main       (       )   {            
               char        v[                       
                100               ]         ,   s  ;
          int t[100   ]                    ,        
              u[100    ]           ;       u        
                  [                         0       
      ]=ftell(stdin        )            ;           
         while(gets (v    )                 )       
                {t[            r ]=                 
             strlen                 (               
               v);y=                                
                  t  [      r             ]         
                 >y             ?        t [        
                  r         ]    :   y;             
              u[++r     ]   =                       
        ftell(stdin )     ;                        }
              while          (                    n 
                  <              y        )         
            {for(x=      0       ;         x        
            <r;x++) {                         s     
               =' '     ;                           
              if(n<             t        [          
                  x            ]     )    {         
        fseek(stdin   , u       [     x    ]        
                +n,0       )                     ;  
         scanf("%c"    ,                     &      
                      s                         )   
                      ;                            }
       printf("%c",                    s      )     
                                            ;  }    
       printf("\n");                n               
                ++;                }             }
```

Vẫn là đoạn code đó nhưng đoạn comment tối nghĩa nay đã trở thành chữ ký `AkatXienPan's Scroll` !!!
