program problem1723;
type
        mas = array[1..27] of byte;
var
        str:string;
        chars:mas;
        i:integer;

function LinearSearch(const A:mas):byte;
var
        max,i,ind:byte;
begin
        max:=A[1];
        ind:=1;
        for i:=2 to 27 do
                if A[i]>max then begin
                        max:=A[i];
                        ind:=i
                end;
        LinearSearch:=ind
end;

begin
        read(str);
        for i:=1 to 27 do
                chars[i]:=0;
        for i:=1 to length(str) do
                inc(chars[Ord(UpCase(str[i]))-Ord('A')+1]);

        writeln(Chr(LinearSearch(chars)+Ord('a')-1));
end.