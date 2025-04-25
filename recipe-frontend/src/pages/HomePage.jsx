import { useState } from 'react'
import { Row, Col, Typography } from 'antd'
import RecipeForm from '../components/RecipeForm'
import RecipeCard from '../components/RecipeCard'

const { Title } = Typography

const HomePage = () => {
  const [recipe, setRecipe] = useState(null)

  return (
    <Row justify="center" style={{ padding: '24px' }}>
      <Col xs={24} md={18} lg={12}>
        <Title level={2} style={{ textAlign: 'center' }}>
          Генератор рецептов
        </Title>
        <RecipeForm onRecipeGenerated={setRecipe} />
        {recipe && <RecipeCard recipe={recipe} />}
      </Col>
    </Row>
  )
}

export default HomePage