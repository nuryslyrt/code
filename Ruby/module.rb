module Stats
   class Dataset
      def initialize(filename)
         IO.foreach(filename) do |line|
         if line[0, 1] == "#"
            print "buldum"
         else
            print "olmadi bastan"
          end
         end
      end
   end
end

initialize(deneme)
