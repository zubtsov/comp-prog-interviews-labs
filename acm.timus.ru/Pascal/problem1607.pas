program problem1607;
var
        a,b,c,d:longint;
begin
        readln(a,b,c,d);
        while (a<c) do begin
                inc(a,b);
                if (a>=c) then begin
                        writeln(c);
                        exit
                end;
                dec(c,d);
                if (a>=c) then begin
                        writeln(a);
                        exit
                end
        end;
        writeln(a);
end.