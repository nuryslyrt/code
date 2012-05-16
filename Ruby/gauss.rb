require 'Matrix'
class Matrix
    def []=(i, j, v)
    	@rows[i][j] = v
    end
 
    def gauss!
  	n = column_size
  	nn = row_size
  	for i in 0..(n-2)
    	    p = -1
    	    for k in i..(nn-1)
      		if @rows[i][k]  != 0
        	    p = k
        	    break
      		end
    	     end
  	     raise "No Solution" if p == -1
    	     if p != i
      	         for h in i..(nn-1) 
        	     @rows[h][i],@rows[h][p] = @rows[h][p],@rows[h][i]
      		 end
    	     end
 
  by  	     for j in (i+1)..nn-1
      		 multiplier = @rows[j][i] / @rows[i][i]
      		 for k in 0..n-1
        	     @rows[j][k] -= multiplier * @rows[i][k]
      	     end
    	 end
     end
     self
 end
 
def gauss
    return clone.gauss!
end
 
def solve
    a = gauss()
    n = row_size()-1
    x = Array.new
    x[n] = a[n,n+1]/a[n,n]
    (n-1).downto(0) { |i|
        sum = 0
        i.upto(n) do  |j|
            sum += a[i, j] *( ( x[j].nil? ) ? 0 : x[j]);
        end
        x[i] = (a[i,n+1]-sum) / a[i, i]
 
    }
    return x
end
 
end

m = Matrix[[8, 7.4, 8.225342], [7.4, 8.72, 10.731329]]
m.solve
