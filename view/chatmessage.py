from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class ChatLogModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self.chat_messages = []

    def rowCount(self, index):
        """Necessary to include rowCount() when subclassing QAbstractListModel. 
        For this program, we only need to update the the number of rows in the model,
        which is based on the length of chat_messages."""
        return len(self.chat_messages)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Necessary to include data() when subclassing QAbstractListModel. Retrieves 
        items from the list and returns data specified by the role, which in this case 
        is displayed as text."""
        if role == Qt.ItemDataRole.DisplayRole:
            return self.chat_messages[index.row()]

    def appendMessage(self, user_input, user_or_chatbot):
        """First, append new messages to chat_messages. Doing so will update the number
        of rows and indexes in the model (rowCount()), which will then update the data()."""
        self.chat_messages.append([user_input, user_or_chatbot])
        # Emit signal to indicate that the layout of items in the model has changed
        self.layoutChanged.emit()

class DrawSpeechBubbleDelegate(QStyledItemDelegate):

    def __init__(self):
        super().__init__()
        self.image_offset = 10 # Horizontal offset for the image 
        # The following variables are used when drawing the speech bubbles
        self.image_size = QSize(48, 48)
        self.side_offset, self.top_offset = 70, 10 
        self.tail_offset_x, self.tail_offset_y = 60, 0
        self.text_side_offset, self.text_top_offset = 90, 20

    def paint(self, painter, option, index):
        """Reimplement the delegate's paint() function. Renders the delegate using the specified QPainter 
        (painter) and QStyleOptionViewItem (option) for the item being drawn at given index (the row value).
        This function paints the item."""
        text, user_or_chatbot = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        image, image_rect = QImage(), QRect() # Initialize objects for the user and chahbot icons
        color, bubble_margins = QColor(), QMargins() # Initialize objects for drawing speech bubbles
        tail_points = QPolygon() # Initialize QPolygon object for drawing the tail on the speech bubbles

        # Use user_or_chatbot value to select the image to display, the color of the pen and the
        # brush. Set the margins for speech bubble. Set the points for the speech bubble's tail.
        # self.image_size.height() = 48 // 2 = 24
        if user_or_chatbot == "chatbot":
            image.load("assert/bot.png")
            image_rect = QRect(QPoint(option.rect.left() + self.image_offset, option.rect.center().y() - 24), self.image_size)
            color = QColor("#C23373")
            bubble_margins = QMargins(self.side_offset, self.top_offset, self.side_offset, self.top_offset)
            tail_points = QPolygon([QPoint(option.rect.x() + self.tail_offset_x, option.rect.center().y()),
                           QPoint(option.rect.x() + self.side_offset, option.rect.center().y() - 5),
                           QPoint(option.rect.x() + self.side_offset, option.rect.center().y() + 5)])
        elif user_or_chatbot == "user":
            image.load("assert/user.png")
            image_rect = QRect(QPoint(option.rect.right() - self.image_offset - self.image_size.width(), option.rect.center().y() - 24), self.image_size)
            color = QColor("#333333")
            bubble_margins = QMargins(self.side_offset, self.top_offset, self.side_offset, self.top_offset)
            tail_points = QPolygon([QPoint(option.rect.right() - self.tail_offset_x, option.rect.center().y()),
                           QPoint(option.rect.right() - self.side_offset, option.rect.center().y() - 5),
                           QPoint(option.rect.right() - self.side_offset, option.rect.center().y() + 5)])

        # Draw the image next to the speech bubble
        painter.drawImage(image_rect, image)

        # Set the QPainter's pen and brush colors; draw the speech bubble and tail
        painter.setPen(color)
        painter.setBrush(color)
        # Remove the margins from the rectangle to shrink its size 
        painter.drawRoundedRect(option.rect.marginsRemoved(bubble_margins), 5, 5)
        painter.drawPolygon(tail_points)

        # Draw the text in the speech bubble
        painter.setPen(QColor(249, 245, 246)) # Reset pen color for the text
        text_margins = QMargins(self.text_side_offset, self.text_top_offset, self.text_side_offset, self.text_top_offset)
        painter.drawText(option.rect.marginsRemoved(text_margins), Qt.AlignmentFlag.AlignVCenter | Qt.TextFlag.TextWordWrap, text)

    def sizeHint(self, option, index):
        """Reimplement to figure out the size of the item displayed at the given index.
        Uses option to figure out the style information, in this case, the margins of the speech bubble."""
        text, user_or_chatbot = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        font_size = QFontMetrics(QFont("Arial", 18))
        text_margins = QMargins(self.text_side_offset, self.text_top_offset, self.text_side_offset, self.text_top_offset)

        # Remove the margins, get the rectangle for the font, and add the margins back in
        rect = option.rect.marginsRemoved(text_margins) 
        rect = font_size.boundingRect(rect, Qt.TextFlag.TextWordWrap, text)
        rect = rect.marginsAdded(text_margins)
        return rect.size()
