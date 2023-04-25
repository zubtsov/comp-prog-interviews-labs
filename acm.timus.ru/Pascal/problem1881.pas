program problem1881;
var
        h,w,n,i,symbols,pages,lines,l:integer;
        s:array[1..10000] of string[100];
begin
        readln(h,w,n);

        for i:=1 to n do
                readln(s[i]);

        pages:=1;
        lines:=1;
        symbols:=0;

        for i:=1 to n do begin
                l:=length(s[i]);
                if (symbols+l <= w) then
                        inc(symbols,l+1)
                else if (lines + 1 <= h) then begin
                        symbols:=l+1;
                        inc(lines) end
                else begin
                        symbols:=l+1;
                        lines:=1;
                        inc(pages) end;
        end;
        writeln(pages)
end.
