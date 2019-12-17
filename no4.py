uses crt;

var i,j,n : Integer;
    p   : array [1..50,1..50] of integer;

Begin
Clrscr;
  write('Jumlah baris data = ');readln(n);
  writeln;

  for i:= 1 to n do
  Begin
       for j:=1 to i do
       Begin
           if(j=1) or (j=i) then
             p[i,j]:=1
           else
             p[i,j]:=p[i-1,j]+p[i-1,j-1];
           write(p[i,j],'    ');
       End;
      writeln;
  End;
  readln;
End.