program problem1792; //èÖêÖÑÖãÄíú))
type
        ham = array[1..7] of byte;
const
        codes:array[1..16] of ham =     ((0,0,0,0,0,0,0),
                                        (1,1,1,1,1,1,1),
                                        (0,0,0,1,1,1,1),
                                        (0,0,1,0,1,1,0),
                                        (0,0,1,1,0,0,1),
                                        (0,1,0,0,1,0,1),
                                        (0,1,0,1,0,1,0),
                                        (0,1,1,0,0,1,1),
                                        (0,1,1,1,1,0,0),
                                        (1,0,0,0,0,1,1),
                                        (1,0,0,1,1,0,0),
                                        (1,0,1,0,1,0,1),
                                        (1,0,1,1,0,1,0),
                                        (1,1,0,0,1,1,0),
                                        (1,1,0,1,0,0,1),
                                        (1,1,1,0,0,0,0));
var
        input_code:ham;
        i:integer;

function nearest(code:ham):byte;
var
        i,j,count:byte;
begin
        for i:=1 to 16 do begin
                count:=0;
                for j:=1 to 7 do
                        if (code[j] <> codes[i,j]) then
                                inc(count);
                if (count <= 1) then begin
                        nearest:=i;
                        break
                end;
        end;
end;

begin
        for i:=1 to 7 do
                read(input_code[i]);
        for i:=1 to 7 do
                write(codes[nearest(input_code),i],' ');
end.