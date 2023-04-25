program problem1636;
var
        T1,T2,x,i:integer;
begin
        readln(T1, T2);
        for i:=1 to 10 do begin
                read(x);
                if (x<>0) then
                        dec(T2,x*20);
        end;
        if (T1<=T2) then
                writeln('No chance.')
        else
                writeln('Dirty debug :(')
end.