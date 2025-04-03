class RandomizedSet
  def initialize(array = [])
    @array = array
  end


=begin
  :type val: Integer
  :rtype: Boolean
=end
  def insert(val)
    return false if @array.include?(val)

    @array.push(val)
    true
  end


=begin
  :type val: Integer
  :rtype: Boolean
=end
  def remove(val)
    return false unless @array.include?(val)

    index = @array.index(val)
    @array.delete_at(index)
    true
  end


=begin
  :rtype: Integer
=end
  def get_random()
    randomIndex = (rand * @array.length).floor
    @array[randomIndex]
  end


end

# Your RandomizedSet object will be instantiated and called as such:
val = 1
obj = RandomizedSet.new()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.get_random()
