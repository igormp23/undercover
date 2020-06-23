from nameko.rpc import rpc, RpcProxy

import game_round_dependencies, schemas

class RoundService:
    
    name = 'round_service'

    database = game_round_dependencies.Database()

    # book_rpc = RpcProxy('book_service')
    # user_rpc = RpcProxy('user_service')

    def __init__(self):
        print("Service Constructor")

    # @rpc
    # def borrow_book(self, id_user, id_book):

    #     result = {
    #         'err': 0,
    #         'msg': ''
    #     }

    #     user = self.user_rpc.verify_user(id_user)
    #     book = self.book_rpc.verify_book(id_book)

    #     bookstatus = self.database.get_book_status(id_book)

    #     if not user and not book:
    #         result['err'] = 1
    #         result['msg'] = 'User is BANNED and Book is LOST'
    #     elif not user:
    #         result['err'] = 1
    #         result['msg'] = 'User is BANNED'
    #     elif not book:
    #         result['err'] = 1
    #         result['msg'] = 'Book is LOST'
    #     elif bookstatus['status'] == 'BORROW':
    #         result['err'] = 1
    #         result['msg'] = 'Book is BORROWED'
    #     else:
    #         self.database.borrow_book(id_user, id_book)
            
    #         self.database.close_connection()
    #         result['msg'] = 'Borrow book SUCESS'

    #     return schemas.CommandResultSchema().dumps(result)

    # @rpc
    # def return_book(self, id, status):

    #     result = {
    #         'err': 0,
    #         'msg': ''
    #     }

    #     if status == 'OK':
    #         self.database.return_book(id, status)
    #         self.database.close_connection()

    #         result['msg'] = 'Return book OK'            
    #     else:
    #         circulation = self.database.get_circulation_by_id(id)

    #         self.user_rpc.ban_user(circulation['id_user'])
    #         self.book_rpc.update_status(circulation['id_book'], "LOST")

    #         self.database.return_book(id, "FAIL")
    #         self.database.close_connection()

    #         result['msg'] = 'Return book FAIL'

    #     return schemas.CommandResultSchema().dumps(result)
        

    def __del__(self):
        print("Service Destructor")