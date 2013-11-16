<?php
/**
 * @Entity(repositoryClass="LocationRepository") @Table(name="locations")
 */
class Location
{
    /**
     * @Id @Column(type="integer") @GeneratedValue
     * @var int
     */
    protected $id;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $address;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $city;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $state;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $zip;

    public function getId()
    {
        return $this->id;
    }

    public function setAddress($address)
    {
        $this->address = $address;
    }

    public function getAddress()
    {
        return $this->address;
    }

    public function setCity($city)
    {
        $this->city = $city;
    }

    public function getCity()
    {
        return $this->city;
    }

    public function setState($state)
    {
        $this->state = $state;
    }

    public function getState()
    {
        return $this->state;
    }

    public function setZip($zip)
    {
        $this->zip = $zip;
    }

    public function getZip()
    {
        return $this->zip;
    }

}
