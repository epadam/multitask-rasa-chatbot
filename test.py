from grakn.client import GraknClient


query = 'match $account isa account; $person isa person, has email "mitchell.gillis@t-online.de";$contract(customer: $person, offer: $account, provider: $bank) isa contract; get $contract;'

query = 'match $mapping isa attribute-mapping, has mapping-key "english customer support", has mapping-value $v;get $v;'

with GraknClient(uri="localhost:48555") as client:
    with client.session(keyspace='banking') as session:
        with session.transaction().read() as tx:
            print("Executing Graql Query: " + query)
            result_iter = tx.query(query)
            # for ans in result_iter:
            #     print(ans.map().get('v'))
            concepts = [ans.map().get('v') for ans in result_iter]
            print(concepts)
            print([c.value() for c in concepts])

# def thing_to_dict(thing, tx):
#     entity = {"id": thing.id, "type": thing.type().label()}

#     for each in thing.as_remote(tx).attributes():
#         entity[each.type().label()] = each.value()
#     return entity


# relation_name = 'contract'

# with GraknClient(uri="localhost:48555") as client:
#     with client.session(keyspace='banking') as session:
#         with session.transaction().read() as tx:
#             print("Executing Graql Query: " + query)
#             result_iter = tx.query(query)

#             relations = []

#             for concept in result_iter:
#                 relation_entity = concept.map().get(relation_name)
                
#                 relation = thing_to_dict(relation_entity, tx)
                
                

                
#                 for (
#                     role_entity,
#                     entity_set,
#                 ) in relation_entity.as_remote(tx).role_players_map().items():
#                     #print(role_entity.label())
#                     role_label = role_entity.label()
#                     thing = entity_set.pop()
#                     #print(thing.attributes())
#                     #print(thing.id, thing.type().label())
#                     entity = {"id": thing.id, "type": thing.type().label()}
#                     for each in thing.attributes():
#                         entity[each.type().label()] = each.value()
                        

#                     relation[role_label] = entity

#                 relations.append(relation)
#             print(relations)
            





# # entity_keys = ["type", "id"]

# # entity = {'id': 'V86144', 'type': 'english-customer-service'}

# # if isinstance(entity_keys, str):
# #     entity_keys = [entity_keys]
# # print(entity_keys)

# # v_list = []
# # for key in entity_keys:
# #     print(type(key))
# #     _e = entity
# #     print('_e =',_e)
# #     for k in key.split("."):
# #         print(k)
# #         _e = _e[k]
# #         print('_e =',_e)

# #     if "balance" in key or "amount" in key:
# #         v_list.append(f"{str(_e)} €")
# #     elif "date" in key:
# #         v_list.append(_e.strftime("%d.%m.%Y (%H:%M:%S)"))
# #     else:
# #         v_list.append(str(_e))
# # print(", ".join(v_list))



# # def thing_to_dict(thing, tx):
# #     entity = {"id": thing.id, "type": thing.type().label()}

# #     for each in thing.as_remote(tx).attributes():
# #         entity[each.type().label()] = each.value()
# #         print(entity)
# #     return entity

# # #match $mapping isa attribute-mapping, has mapping-key 'name', has mapping-value $v; get;

# # query = "match $bank isa bank; get $bank;"

# # with GraknClient(uri="localhost:48555") as client:
# #     with client.session(keyspace="banking") as session:
# #         with session.transaction().read() as tx:
# #             result_iter = tx.query(query).get()

# #             entities = []

# #             concept_maps =[ ans for ans in result_iter]

# #             for concept_map in concept_maps:
                
# #                 concept = concept_map.map().get('bank')
                
# #                 print(concept)
            
                
# #                 entities.append(thing_to_dict(concept, tx))
                    
                    
                
# #                 print('------')
                
#                 # print(entities)
#                 # print('----------------------------')
         

            

#             # bank =[]

#             # for answer in result_iter:
#             #     #bank.append(answer.map())
#             #     w = answer.map().get('bank')
#             #     #print(w['bank'].as_remote(tx).attributes())
#             #     for k in w.as_remote(tx).attributes():
#             #         print(k.value())
#                 #print(w['name'].type().label())
#                 # for a in w.as_remote(tx).attributes():
#                 #     print(a.id)
#                 # print('------')

#             #print(bank[0]['bank'].value())

#             #entity = {"id": a.id, "type": a.type().label()}
#             #         #for each in b:
#             #         entity[a.type().label()] = a.value()

#             # print(bank[0].type().label())   
#             # entities =[]
#             # for 
            
                
                
#                 #bank.append(answer.map())
#                 # print(bank.get('n').value())

#             #print(bank[0].get('a').attributes())
            
#             # entities =[]
#             # for b in bank:
#             #     for a in b:
#             #         entity = {"id": a.id, "type": a.type().label()}
#             #         #for each in b:
#             #         entity[a.type().label()] = a.value()
#             #     entities.append(entity)

            

            
               
      


#             # entities = []

#             # for concepts in result_iter:
#             #     print(concepts) #conceptmap
#             #     entities = concepts.map().get("v")
#             #     print(entities)
            
#             # for c in entities:
#             #     for a in c.as_remote(tx).attributes():
#             #         print(a)
#             #         #entities.append(self._thing_to_dict(a))
       


#             # concepts = [ans.get('v') for ans in result_iter]
#             # for c in concepts:
#             #     print(c)
#             #     entities = []
#             #     for a in c.as_remote(tx).attributes():
#             #         entity = {"id": a.id, "type": a.type().label()}
#             #         for each in a.attributes():
#             #             entity[each.type().label()] = each.value()



#                 #     entity[each.type().label()] = each.value()

#                 #     entities.append(self._thing_to_dict(a))
          
#                 # relation_entity = concept.map().get("contract") # concept
#                 # print(relation_entity.is_relation())
                
#                 # entity = {"id": relation_entity.id, "type": relation_entity.type().label()}
#                 # for each in relation_entity().type():
#                 #     print(each)

#                 #     entity[each.type().label()] = each.value()
                



#             # concepts = [ans.get('v') for ans in answer_iterator]
 

#             # for c in concepts:
#             #     for a in c.as_remote(tx).attributes():
#             #         print(a.value())
#             #a = [c.value() for c in concepts]
            






#             #banks = answer_iterator.get("value")
#             # concepts = [ans for ans in answer_iterator]
#             # print(concepts)
#             # k = 0
#             # for c in concepts:
#             #     a = c.map()
#             #     print(a.id)
                
       

             



#             # print(concepts[0])

#             # for c in concepts:
                
#             #     print(c.map())
#             #     a = c.map()

#             #   print(a.values())
#                 # print(a.get('v'))
#                 # for x in a:
#                 #     print(x)


#             # entities = []
#             # for c in concepts:
#             #     entities.append(thing_to_dict(c))
#             # print(entities)   
#             # print(answer_iterator)
#             # print('success')

# # concepts = result_iter.collect_concepts()
#                     # return [c.value() for c in concepts]