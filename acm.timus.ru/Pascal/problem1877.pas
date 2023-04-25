program problem1877;
var
        code1, code2:string[4];
        c1,c2:integer;
begin
        readln(code1);
        readln(code2);
        val(code1,c1);
        val(code2,c2);
        if (odd(c2)) or (not odd(c1)) then
                writeln('yes')
        else
                writeln('no')
end.