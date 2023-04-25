program problem1313;
type
        mas = array[1..100, 1..100] of byte;
var
        A:mas;
        i,j,n:integer;
begin
        readln(n);
        for i:=1 to n do
                for j:=1 to n do
                        read(A[i,j]);
        for i:=1 to n do
                for j:=0 to (i-1) do
                        write(a[i-j,1+j],' ');
        for i:=2 to n do
                for j:=0 to (n-i) do
                        write(A[n-j,i+j],' ');

end.