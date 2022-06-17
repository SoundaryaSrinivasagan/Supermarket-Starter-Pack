# importing sys
import sys

# adding sample_data to the system path
sys.path.insert(0, '/Desktop/Supermarket-Starter-Pack/sample_data')

class checkout_counter:
      '''
       Function:         total_cost_before_tax(trans_num)
       Description:      This function will return the number of items present in any transaction before taxes
       Input Parameters: trans_num : Int
                                     trans_num is the number of the transaction you want to pull from transaction_data
      '''
      def total_cost_before_tax (trans_num):
        cost = 0
        for item in transaction_no(trans_num):
          cost = cost + item_dict[item]

        return(cost)

      '''
       Function:         find_total(trans_num)
       Description:      This Function should be able to find the final price of any transaction after Taxes have been implemented
       Input Parameters: trans_num : Int
                                     trans_num is the number of the transaction you want to pull from transaction_data
      '''
      def find_total(trans_num):
      # Note that the taxes are assumed to be 5%, but they can be modified to the actual HST with respect to your country
        final_price = total_cost_before_tax(trans_num) * 1.05

        return(final_price)


