program problem1083;
var
        n,k:integer;
        str:string[21];
function fact(n,k:longint):longint;
begin
        if (n-k) > 0 then
                fact:=n*fact(n-k, k)
        else
                fact:=1
end;

begin
        read(n);
        read(str);
        k:=length(str)-1;

        if (n mod k = 0) then
                writeln(fact(n,k)*k)
        else
                writeln(fact(n,k)*(n mod k))
end.