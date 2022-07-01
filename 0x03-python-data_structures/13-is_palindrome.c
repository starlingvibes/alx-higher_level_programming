#include "lists.h"

/**
 * palindrome_helper - helper function
 *  @head: double pointer to head
 * @end: pointer to end
 */
int palindrome_helper(listint_t **head, listint_t *end)
{
    if (end == NULL){
        return (1);
    }
    if (palindrome_helper(head, end->next) && (*head)->n == end->n)
    {
        *head = (*head)->next;
        return (1);
    }
    return (0);
}

/**
 * is_palindrome - palindrome or not
 * @head: double pointer to pointer of head
 * Return: 1 if it's a palindrome
 * 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL) {
        return (1);
    }
    return (palindrome_helper(head, *head));
}

