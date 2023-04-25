program problem1545;
var
        n,i:integer;
        s:array[1..1000] of string[2];
        c:char;
begin
        readln(n);
        for i:=1 to n do
                readln(s[i]);
        readln(c);
        for i:=1 to n do
                if (s[i][1]=c) then
                        writeln(s[i]);
end.