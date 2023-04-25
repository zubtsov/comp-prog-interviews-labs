program problem1820;
uses math;
var
        k,n:word;
begin
        readln(n,k);
        if (n<=k) then
                writeln(2)
        else
                writeln(2*n div k + sign(2*n mod k))
end.
