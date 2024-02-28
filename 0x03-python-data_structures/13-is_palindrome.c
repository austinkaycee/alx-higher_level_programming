#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    int len = 0, i;
    int *arr;
    listint_t *current;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    current = *head;
    while (current != NULL)
    {
        len++;
        current = current->next;
    }

    arr = malloc(sizeof(int) * len);
    if (arr == NULL)
        return (0);

    current = *head;
    for (i = 0; i < len; i++)
    {
        arr[i] = current->n;
        current = current->next;
    }

    for (i = 0; i < len / 2; i++)
    {
        if (arr[i] != arr[len - 1 - i])
        {
            free(arr);
            return (0);
        }
    }

    free(arr);
    return (1);
}

