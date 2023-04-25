program problem1712;
const
        N=4;
type
        mas = array[1..N,1..N] of char;
        psw = string[N*N];
var
        grid,symbols:mas;
        i,j:integer;
        pass:psw;

procedure read_matrix(var A:mas);
var
        i,j:integer;
begin
        for i:=1 to N do begin
                for j:=1 to N do
                        read(A[i,j]);
                readln;
        end;
end;

procedure apply_grid(const A,B:mas;var pstr:psw);
var
        i,j:integer;
begin
        for i:=1 to N do
                for j:=1 to N do
                        if (A[i,j]='X') then
                                pstr:=pstr+B[i,j];
end;

procedure rotate_matrix(var A:mas; B:mas);
var
        i,j,p:integer;
        m:char;
begin
        for i:=1 to N do
                for j:=1 to N do
                        A[j,i]:=B[i,j];

        for i:=1 to N do begin
                p:=0;
                for j:=1 to N div 2 do begin
                        m:=A[i,j];
                        A[i,j]:=A[i,N-p];
                        A[i,N-p]:=m;
                        inc(p);
                end;
        end;
end;

begin
        read_matrix(grid);
        read_matrix(symbols);
        for i:=1 to N do begin
                apply_grid(grid,symbols,pass);
                rotate_matrix(grid,grid);
        end;
        writeln(pass);
end.