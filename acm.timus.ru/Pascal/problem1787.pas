program problem1787;
var
        k,n,s,a,i:word; //�ய�᪭�� ᯮᮡ����� ��設/���, ���-�� �����...
begin
        s:=0;
        readln(k,n);

        for i:=1 to n do begin
                read(a);
                s:=s+a;
                if (s>k) then
                        s:=s-k
                else
                        s:=0
        end;
        writeln(s);
end.