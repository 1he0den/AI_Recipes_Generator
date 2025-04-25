import { Card, Image, List, Tag, Space, Divider } from 'antd'
import { ClockCircleOutlined, FireOutlined } from '@ant-design/icons'

const RecipeCard = ({ recipe }) => {
  return (
    <Card
      title={recipe.title}
      style={{ marginTop: 24 }}
      cover={
        recipe.image_url && (
          <Image
            src={recipe.image_url}
            alt={recipe.title}
            preview={false}
          />
        )
      }
    >
      <Space size="middle">
        <Tag icon={<ClockCircleOutlined />} color="blue">
          {recipe.cooking_time} мин
        </Tag>
        <Tag icon={<FireOutlined />} color="orange">
          {recipe.difficulty}
        </Tag>
      </Space>

      <Divider orientation="left">Ингредиенты</Divider>
      <List
        size="small"
        dataSource={recipe.ingredients}
        renderItem={(item) => <List.Item>{item}</List.Item>}
      />

      <Divider orientation="left">Приготовление</Divider>
      <List
        dataSource={recipe.instructions}
        renderItem={(step, index) => (
          <List.Item>
            <strong>{index + 1}.</strong> {step}
          </List.Item>
        )}
      />
    </Card>
  )
}

export default RecipeCard