#include <iostream>

using namespace std;

class Single_list
{
    public:
    int val;
    Single_list* next;

    Single_list* createNode(int a)
    {
        Single_list* new_val = new Single_list();
        new_val->val = a;
        new_val->next = NULL;
        return new_val;
    }

    Single_list* insertNode(Single_list* end_node, int a)
    {
        Single_list* new_node = createNode(a);
        end_node->next = new_node;
        return new_node;
    }

    void insertAtPos(Single_list** start_node, int a, int pos)
    {
        Single_list* new_node = createNode(a);
        if((*start_node)==NULL)
        cout<<"list overflow\n";
        else
        {
            if(pos==1)
            {
                new_node->next = *start_node;
                (*start_node) = new_node;
            }
            else
            {
                insertAtPos(&((*start_node)->next),a,pos-1);   
            }
        }
    }

    void deleteNode(Single_list** start_node,int a)
    {
        if(*start_node == NULL)
        cout<<"Mem Overflow";
        else
        {
            if((*start_node)->val==a)
            *start_node = (*start_node)->next;
            else
            deleteNode(&((*start_node)->next),a);
        }   
    }

    void printList(Single_list* start_node)
    {
        Single_list* iter = start_node;
        while(iter!= NULL)
        {
            cout<<iter->val<<" ";
            iter = iter->next;
        }
        cout<<"End of list\n";
    }
    
};
int main()
{
    Single_list list;
    Single_list* start = list.createNode(1);
    // cout<<start->val<<endl;
    Single_list* end_node = list.createNode(start->val);
    start->next = end_node;
    // list.printList(start);
    // cout<<start->next->val;
    for(int i=0 ; i<10 ; i++)
    end_node = list.insertNode(end_node,i);
    // list.printList(start);
    list.insertAtPos(&start,11,1);
    list.printList(start);
    list.deleteNode(&start,11);
    list.printList(start);
    
}