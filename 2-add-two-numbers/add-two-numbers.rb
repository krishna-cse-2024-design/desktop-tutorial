# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    root = nil
    prev = nil
    carry = 0

    loop do
        break if l1.nil? && l2.nil?

        a = l1&.val.to_i
        b = l2&.val.to_i
        l1 = l1&.next
        l2 = l2&.next

        c = a + b + carry
        carry = c/10
        value = c%10

        node = ListNode.new(value)
        if root.nil?
            prev = node
            root = node
        else
            prev.next = node
            prev = node
        end
    end

    if carry > 0
        node = ListNode.new(carry)
        prev.next = node
    end

    root
end